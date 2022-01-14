import os
import random
import string
import requests


def midia_uploader():
    headers = {
        'authority': 'upload-business.facebook.com',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://business.facebook.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://business.facebook.com/',
        'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,la;q=0.6',
        'cookie': 'sb=K0TQYRAzIfDXx2uTaDWZ7cLs; datr=K0TQYWlX0gWugsp2_eFI5bUv; c_user=100002268548853; _fbp=fb.1.1641333987217.1480922705; spin=r.1004937638_b.trunk_t.1642106489_s.1_v.2_; xs=7%3APREnY6Uh_hkNuw%3A2%3A1641038957%3A-1%3A1161%3A%3AAcVNvagv7wxOMxhmh-CIzZMLvkaexkiZGRC7CcCusqI; fr=0ik1ka9UYPKSBa8Yg.AWUBB8-WvKyS20_wXSHQtVAp_OA.Bh4JM8.q3.AAA.0.0.Bh4JM8.AWVrNeaa5Os; usida=eyJ2ZXIiOjEsImlkIjoiQXI1bzN0cG1kMHlibiIsInRpbWUiOjE2NDIxMDk1MzN9; wd=873x635',
    }

    params = (
        ('av', '105349341511172'),
        ('__usid', '6-Tr5o3tptqyhuv:Pr5o3s62uvjnc:0-Ar5o3tpmd0ybn-RV=6:F='),
        ('__user', '100002268548853'),
        ('__a', '1'),
        ('__dyn', '7xeUmBz8fXgydwn8yEqxenFG3a2q12wAxuq3O1FDyUJ3odF98SmqbxW4E2czoboGq58985i0x8C4Uqx60DU4m1qwcy1lCyU4a3a1ag4K2C0A8swIK2i1gwwAwXwEwgolzU1vrzouwg85W7o8o46u2C2l0Fwwwi85W1ywnEfogwNxaU5afxW1xwCxe6888aE7614zobEaUiwBwOwywnEcU6y4EkyE2Gxe19wAyVUpwSyES0gq'),
        ('__csr', ''),
        ('__req', '11'),
        ('__hs', '19005.BP:bizweb_pkg.2.0.0.0.'),
        ('dpr', '1'),
        ('__ccg', 'EXCELLENT'),
        ('__rev', '1004937638'),
        ('__s', 't9er86:nqahlz:alfg9x'),
        ('__hsi', '7052806501256320881-0'),
        ('__comet_req', '0'),
        ('fb_dtsg', 'AQEBuUoQomzxQtU:7:1641038957'),
        ('jazoest', '22114'),
        ('lsd', 'nruSxFDRejhquB1eY5vgoa'),
        ('__spin_r', '1004937638'),
        ('__spin_b', 'trunk'),
        ('__spin_t', '1642109477'),
        ('__jssesw', '1'),
    )

    data = {
        'source': 8,
        'profile_id': 100002268548853,
        'waterfallxapp': "web_react_composer",
        'upload_id': 1030
    }
    filename = "D:/1.jpg"
    files = {'farr': (os.path.basename(filename), open(
        filename, 'rb'), 'application/octet-stream')}

    response = requests.post('https://upload-business.facebook.com/ajax/react_composer/attachments/photo/upload',
                             headers=headers, params=params, data=data, files=files)

    print(response.content)
    print(response.status_code)


def id_generator(size=5, chars=string.digits):

    composer_session_id = "a7418c51-3d95-478c-9fca-"
    return composer_session_id + ''.join(random.choice(chars) for _ in range(size))


def story_poster():

    headers = {
        'authority': 'business.facebook.com',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'viewport-width': '873',
        'x-fb-friendly-name': 'BusinessComposerStoryCreationMutation',
        'x-fb-lsd': 'nruSxFDRejhquB1eY5vgoa',
        # atencao. sempre retirar contet-type do header
        # 'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://business.facebook.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://business.facebook.com/latest/posts/published_posts?nav_ref=bm_home_redirect',
        'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,la;q=0.6',
        'cookie': 'sb=K0TQYRAzIfDXx2uTaDWZ7cLs; datr=K0TQYWlX0gWugsp2_eFI5bUv; c_user=100002268548853; _fbp=fb.1.1641333987217.1480922705; spin=r.1004937638_b.trunk_t.1642106489_s.1_v.2_; xs=7%3APREnY6Uh_hkNuw%3A2%3A1641038957%3A-1%3A1161%3A%3AAcVNvagv7wxOMxhmh-CIzZMLvkaexkiZGRC7CcCusqI; fr=0ik1ka9UYPKSBa8Yg.AWUBB8-WvKyS20_wXSHQtVAp_OA.Bh4JM8.q3.AAA.0.0.Bh4JM8.AWVrNeaa5Os; wd=873x635; usida=eyJ2ZXIiOjEsImlkIjoiQXI1b2NrNDExY3N4MHMiLCJ0aW1lIjoxNjQyMTIwODUyfQ%3D%3D',
    }

    data = {
        'av': '105349341511172',
        '__usid': '6-Tr5o3tptqyhuv:Pr5o3s62uvjnc:0-Ar5ock411csx0s-RV=6:F=',
        '__user': '100002268548853',
        '__a': '1',
        '__dyn': '7xeUmBz8fXgydwn8yEqxenFG3a2q12wAxuq3O1FDyUJ3odF98SmqbxW4E2czoboGq58985i0x8C4Uqx60DU4m1qwcy1lCyU4a3a1ag4K2C0A8swIK2i1gwwAwXwEwgolzU1vrzouwg85W7o8o46u2C2l0Fwwwi85W1ywnEfogwNxaU5afxW1xwCxe6888aE7614zobEaUiwBwOwywnEcU6y4EkyE2Gxe19wAyVUpwSyES0gq',
        '__csr': '',
        '__req': '1f',
        '__hs': '19005.BP:bizweb_pkg.2.0.0.0.',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1004937638',
        '__s': '2psi70:nqahlz:alfg9x',
        '__hsi': '7052806501256320881-0',
        '__comet_req': '0',
        'fb_dtsg': 'AQEBuUoQomzxQtU:7:1641038957',
        'jazoest': '22114',
        'lsd': 'nruSxFDRejhquB1eY5vgoa',
        '__spin_r': '1004937638',
        '__spin_b': 'trunk',
        '__spin_t': '1642109477',
        '__jssesw': '1',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'BusinessComposerStoryCreationMutation',
        'variables': r'''{
            "input":{
                "client_mutation_id":"1",
                "base":{"actor_id":"105349341511172",
                "composer_entry_point":"biz_web_content_manager_published_posts_tab_stories",
                "source":"WWW",
                "unpublished_content_data":null,
                "attachments":[
                    {"photo":{
                        "id":"315612273818210",
                        "story_call_to_action_data":null}}],
                        "story_original_attachments_data":[
                            {
                                "original_photo_id":"315612273818210",
                                "burned_photo":{
                                    "story_call_to_action_data":null,
                                    "id":"315612273818210"}}]},
                                    "channels":["FACEBOOK_STORY","INSTAGRAM_STORY"],
                                    "identities":["105349341511172","18241397278045046"],
                                    "logging":{
                                        "composer_session_id":"a7418c51-3d95-478c-9fca-941948bc9722"}}}
                                        ''',
        'server_timestamps': 'true',
        'doc_id': '3835120259908410'
    }

    response = requests.post(
        'https://business.facebook.com/api/graphql/', headers=headers, data=data)

    print(response.content)
    print(response.status_code)


story_poster()
