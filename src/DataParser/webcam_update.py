import os
import re
import datetime
import json

STATIC_ROOT = os.getenv('STATIC_ROOT')  # Something like 'path/to/project/mdf/static/'
JSON_ROOT = os.path.join(STATIC_ROOT, 'mdfserver', 'json')
GAMUT_PHOTOS_DIR = os.path.join(STATIC_ROOT, 'mdfserver', 'images', 'gamutphotos')
DIR_REGEX = re.compile('(?P<host>^[A-Z]{2,})_(?P<site>([A-Z]{2,}_){2}[A-Z]+)$', re.IGNORECASE)
FILE_REGEX = re.compile('.*([0-9]*_)?(?P<site>([a-z]+_)+[a-z]+)_{1,2}(?P<date>\d{4}_(\d{2}_){4}\d{2})\.jpg$', re.IGNORECASE)
MIN_FILE_SIZE = 5000
SITES_TO_SHOW = ['PR_CH_AA', 'PR_SC_Canal', 'LR_FB_BA', 'LR_TWDEF_C', 'RB_FD_AA', 'RB_KF_BA']
NETWORK_CODES = {'LoganSite.json': 'Logan', 'ProvoSite.json': 'Provo', 'RedButteSite.json': 'RedButte'}
INACTIVE_DATE = datetime.datetime.now() - datetime.timedelta(days=14)


def get_latest_webcam_photos():
    site_photos = {}
    dirs = os.listdir(GAMUT_PHOTOS_DIR)
    for folder in dirs:
        folder_match = DIR_REGEX.match(folder)
        if not folder_match:
            continue
        temp_date = '2000_00_00_00_00_00'
        temp_name = ''
        for filename in os.listdir(os.path.join(GAMUT_PHOTOS_DIR, folder)):
            re_match = FILE_REGEX.match(filename)
            if re_match is None or temp_date > re_match.groupdict()['date']:
                continue
            if os.path.getsize(os.path.join(GAMUT_PHOTOS_DIR, folder, filename)) < MIN_FILE_SIZE:
                continue
            temp_date = re_match.groupdict()['date']
            temp_name = filename
        if temp_name != '':
            photo_date = datetime.datetime.strptime(temp_date, '%Y_%m_%d_%H_%M_%S')
            site_photos[folder_match.groupdict()['site']] = {'date': str(photo_date), 'dir': folder, 'name': temp_name, 'active': photo_date > INACTIVE_DATE}
    return site_photos


def get_site_info():
    sites = {}
    latest_photos = get_latest_webcam_photos()
    all_photos = get_site_photos
    json_site_files = ['LoganSite.json', 'ProvoSite.json', 'RedButteSite.json']
    for site_file in json_site_files:
        sites[NETWORK_CODES[site_file]] = {}
        temp = json.loads(open(os.path.join(STATIC_ROOT, 'mdfserver', 'json', site_file)).read())
        for key in temp.keys():
            if key in latest_photos.keys():
                temp_site_info = {'lat': str(temp[key]['info']['latitude']), 'lon': str(temp[key]['info']['longitude']),
                                  'site_name': temp[key]['info']['name'], 'img_name': latest_photos[key]['name'],
                                  'img_dir': latest_photos[key]['dir'], 'img_date': latest_photos[key]['date'], 'active_webcam': latest_photos[key]['active']}
                sites[NETWORK_CODES[site_file]][key] = temp_site_info
    return sites


def get_site_photos():
    site_photos = {}
    dirs = os.listdir(GAMUT_PHOTOS_DIR)
    for folder in dirs:
        folder_match = DIR_REGEX.match(folder)
        if not folder_match:
            continue
        temp_date = '2000_00_00_00_00_00'
        temp_name = ''
        for filename in os.listdir(os.path.join(GAMUT_PHOTOS_DIR, folder)):
            re_match = FILE_REGEX.match(filename)
            if re_match is None or os.path.getsize(os.path.join(GAMUT_PHOTOS_DIR, folder, filename)) < MIN_FILE_SIZE:
                continue
            if folder not in site_photos:
                site_photos[folder] = []
            photo_date = datetime.datetime.strptime(re_match.groupdict()['date'], '%Y_%m_%d_%H_%M_%S')
            site_photos[folder].append({'date': str(photo_date), 'site': folder_match.groupdict()['site'], 'name': filename})

    for folder in site_photos.keys():
        site_list = site_photos[folder].sort(key=lambda x:x['date'], reverse=True)

    return site_photos


def main():
    file_out = open(os.path.join(GAMUT_PHOTOS_DIR, 'webcam_details.json'), 'w')
    file_out.write(json.dumps(get_site_info()))

    file_out = open(os.path.join(GAMUT_PHOTOS_DIR, 'ordered_dir_listings.json'), 'w')
    file_out.write(json.dumps(get_site_photos()))


if __name__ == "__main__":
    main()
