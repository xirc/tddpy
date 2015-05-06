from fabric.api import env, run


APP = 'tddpy-staging'

def _get_base_folder(site):
    return '~/sites/' + site

def _get_manage_do_py(site):
    return '{path}/virtualenv/bin/python {path}/source/manage.py'.format(
        path=_get_base_folder(site)
    )


def reset_database():
    run('{manage_py} flush --noinput'.format(
        manage_py=_get_manage_do_py(APP)
    ))

def create_session_on_server(email):
    session_key = run('{manage_py} create_session {email}'.format(
        manage_py=_get_manage_do_py(APP),
        email=email,
    ))
    print(session_key)
