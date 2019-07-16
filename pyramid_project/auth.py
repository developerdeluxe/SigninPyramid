from pyramid.view import view_config

# @view_config(route_name='test', renderer='templates/test.pt')
# def test_view(request):
#     return {'newmess': 'New View File also work'}


@view_config(route_name='signin', renderer='templates/signin.pt')
def signin_view(request):
    # print(request.method)
    if request.method == 'POST':
        print(request.body)
        return {'mess': 'Thanks to register to our Website'}
    # print(request.body)
    return {'mess': 'Welcome to our website'}