import random

apps = [
    [ 'manager-for-gphotos-pro', 'b3ff4e3c-9d32-4615-90e2-0647ae66f595'],
    [ 'gclient-for-google-photos-pro', 'ed1d5a9b-7fd1-4213-9f3c-290f501ba578'],
    [ 'studio-photo-collage', '53ad363c-2cc7-48f9-973c-ba83acf8e9b2'],
    [ 'screen-shot-tool', 'c49a71b8-5db1-4685-8cc7-f4a744869dad'],
    [ 'jack-for-pdf', '835592b4-aaf6-41bd-b28d-01ee7d9c7730'],
    [ 'templates-for-contract', 'e4ae7028-badd-4334-8419-0babcf825ef3'],
    [ 'cvs-resume-templates', '4e6a26c0-fa1a-49fb-94b1-0f50aa1bfcc8'],
    [ 'word-files-editor', '9ce26cab-43c4-4b42-be7e-1c69abb2c421'],
    [ 'editor-for-excel-files', '422f4a69-35fd-43de-b1bd-21b0b20d8c49'],
    [ 'messenger-for-google-hangouts-pro', '30a946b8-d538-4b5e-8087-236007c86045'],
    [ 'rar-zip-extractor-pro', '102c291b-e42a-49e4-97cd-354bbaca3544']
]

class SiteApp:
    """Tool for work with site

    Attributes:
        id     Unique sequence numbers and letters for indeficient app
        name   Name application.
    """

    def __init__(self, info: list):
        self.name = info[0]
        self.id = info[1]

    def get_screens(self) -> list:
        "Return list of links on img app"
        res = []
        for i in range(0, 4):
            res.append('/images/uploaded/' + self.name + '/screens/' + str(i) + '.jpg')
        return res

    def get_installer(self) -> str:
        "Return link on download application installer"
        return '/ru-ru/store/downloadapplicationinstaller?applicationId=' + self.id

    def get_page_application(self) -> str:
        "Return link on page with application name"
        return '/ru-ru/store/details/' + self.name


def get_random_app() -> SiteApp:
    return SiteApp(random.choice(apps))