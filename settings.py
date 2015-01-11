RESOURCE_METHODS = ['GET','POST','DELETE']

ITEM_METHODS = ['GET','PATCH','DELETE']

DOMAIN = {
    'user': {
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username',
            },
        'schema': {
            'firstname': {
                'type': 'string'
            },
            'lastname': {
                'type': 'string'
            },
            'username': {
                'type': 'string'
            },
	    'password': {
		'type': 'string'
	    },
            'phone': {
                'type': 'string'
            }
        }
    },
    'item': {
        'schema': {
            'name':{
                'type': 'string'
                },
            'username': {
                'type': 'string'
                }
            },
        'resource_methods': ['GET', 'POST','DELETE'],
        }
}
