import praw
import webbrowser
r = praw.Reddit('OAuth testing example by u/moosekin/ ver 0.1')

r.set_oauth_app_info(client_id='PILWqm0804TEAA',
	client_secret='gTFauLHWoUkEndnODGJgCiy1qJ4',
	redirect_uri='http://127.0.0.1:65010/authorize_callback')

#url = r.get_authorize_url('uniqueKey', 'identity', True)
#webbrowser.open(url)

access_information=r.get_access_information('6GuN0DXMI-IBXLV5yfBz0Q6Q938')
r.set_access_credentials(**access_information)

authenticated_user = r.get_me()
print authenticated_user.name, authenticated_user.link_karma

