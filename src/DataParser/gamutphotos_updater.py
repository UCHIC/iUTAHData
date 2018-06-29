import os, errno, shutil, json, logging
from requests import Request, Session, PreparedRequest

GAMUTPHOTOS_ROOT = os.environ['GAMUTPHOTOS_ROOT']
STATIC_PHOTO_URL = 'http://data.iutahepscor.org/mdf/static/mdfserver/images/gamutphotos/{0}'

class GamutPhotoUpdater(object):
    """
    Gets latest webcam detail info from data.iutahepscor.org and downloads images into specified directory.
    """

    WEBCAM_DETAILS = 'webcam_details.json'

    def __init__(self):
        self.session = Session()
        self.session.headers.update({'Content-Type': 'application/json; charset=utf8'})

    def _get_webcam_details(self):
        req = self.session.get(STATIC_PHOTO_URL.format(self.WEBCAM_DETAILS))

        res = req.json()

        fp = os.path.join(GAMUTPHOTOS_ROOT, 'webcam_details.json')
        with open(fp, 'w') as fout:
            json.dump(res, fout, indent=4)

        return res

    def update_photos(self):
        site_images = []
        try:
            details = self._get_webcam_details()
            for network_key, network in details.iteritems():

                for site_key, site in network.iteritems():
                    image_dir = site.get('img_dir', None)
                    image_name = site.get('img_name', None)

                    if image_dir and image_name:
                        site_images.append(SiteImage(image_dir, image_name))

        except Exception as e:
            logging.error(e)

        image_requester = ImageRequester()
        image_requester.get_photos(site_images)


class SiteImage(object):
    def __init__(self, par_dir, name, image=None):
        """
        :param par_dir: The image's parent directory
        :param name: The filename of the image
        """
        self.par_dir = par_dir
        self.name = name
        self.image = image
        self.prepped = None

    def prepare_request(self, session):  # type: (Session) -> PreparedRequest
        path = "{0}/{1}".format(self.par_dir, self.name)
        req = Request('GET', STATIC_PHOTO_URL.format(path))
        self.prepped = session.prepare_request(req)

        return self.prepped

    def save(self):
        if self.image is None:
            return

        directory = os.path.join(GAMUTPHOTOS_ROOT, self.par_dir)

        try:
            os.makedirs(directory)
        except OSError as err:
            if err.errno == errno.EEXIST and os.path.isdir(directory):
                pass
            else:
                raise

        file_path = "%s/%s" % (directory, self.name)
        with open(file_path, 'wb') as fout:
            shutil.copyfileobj(self.image, fout)


class ImageRequester(object):
    def __init__(self):
        self.session = Session()

    def get_photos(self, site_images):  # type: ([SiteImage]) -> None

        logging.info('Retrieving images...')

        # Request images from data.iutahepscor.org
        for image in site_images:  # type: SiteImage
            preq = image.prepare_request(self.session)

            resp = self.session.send(preq, stream=True)

            if resp.status_code == 200:
                logging.debug('Image downloaded: {0}/{1} OK'.format(image.par_dir, image.name))
                image.image = resp.raw
            else:
                logging.warn('Image download failed for: {0}/{1} ({2})'.format(
                    image.par_dir, image.name, resp.status_code))

        # Save images to disk
        for image in site_images:
            image.save()


def main():
    updater = GamutPhotoUpdater()
    updater.update_photos()


__all__ = [
    'GamutPhotoUpdater',
    'SiteImage',
    'ImageRequester'
]

if __name__ == "__main__":
    main()
