import logging
from datetime import timedelta
import pandas
from sqlalchemy.orm.exc import NoResultFound

from DataParser.odmdata import DataValue
from DataParser.odmdata import ODMVersion
from DataParser.odmdata import QualityControlLevel
from DataParser.odmdata import Series
from DataParser.odmdata import SessionFactory
from DataParser.odmdata import Site

logger = logging.getLogger('main')

DAY_LIMIT = 96


class SeriesService:
    # Accepts a string for creating a SessionFactory, default uses odmdata/connection.cfg
    def __init__(self, connection_string="", debug=False):
        self._session_factory = SessionFactory(connection_string, debug)
        self._edit_session = self._session_factory.get_session()
        self._debug = debug

    def reset_session(self):
        self._edit_session = self._session_factory.get_session()  # Reset the session in order to prevent memory leaks

    def get_db_version(self):
        return self._edit_session.query(ODMVersion).first().version_number

    def get_all_sites(self):
        return self._edit_session.query(Site).all()

    def get_raw_qc_level_id(self):
        return self._edit_session.query(QualityControlLevel.id).filter_by(definition='Raw data').first().id

    def get_site_series_by_variable_codes(self, site_id, qc_level, variable_codes):
        return self._edit_session.query(Series)\
            .filter_by(site_id=site_id, quality_control_level_id=qc_level)\
            .filter(Series.variable_code.in_(variable_codes))\
            .all()

    def get_site_last_observation_time(self, site_id):
        try:
            return self._edit_session.query(DataValue.local_date_time)\
                .filter_by(site_id=site_id).order_by(DataValue.local_date_time.desc()).limit(1).one()[0]
        except NoResultFound:
            return None

    def get_site_variables_raw_values(self, site_id, qc_level_id, variables_ids, observation_time):
        values = self._edit_session.query(DataValue.variable_id, DataValue.local_date_time, DataValue.data_value)\
            .filter_by(site_id=site_id, quality_control_level_id=qc_level_id)\
            .filter(DataValue.variable_id.in_(variables_ids))\
            .filter(DataValue.local_date_time >= (observation_time - timedelta(hours=24)))\
            .order_by(DataValue.local_date_time.desc())

        query = values.statement.compile(dialect=self._session_factory.engine.dialect)
        return pandas.read_sql_query(sql=query, con=self._session_factory.engine, params=query.params)
