from pyramid.view import view_config


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'Pyramid_project'}


@view_config(route_name='check', renderer='templates/dashboard.pt')
def dashboard_view(request):
    return {'mess': 'Welcome to the Dashboard Admin'}

# @view_config(route_name='test', renderer='templates/test.pt')
# def test_view(request):
#     return {'newmess': 'New View File also work'}
