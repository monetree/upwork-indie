#Api documentation 

### api endpoints for get endpoints:

- `/release/`

	- query paramms
		- title
		- artist_name
		- slug
		- artist_id
		- date_range
		- limit
		- offset

	- orders
		- id
		- title
		- slug
		- created_on

- `/product/`

	- query paramms
		- name
		- artist_name
		- artist_id
		- date_range
		- limit
		- offset

	- orders
		- id
		- name
		- created_on
                    
###Tables
                    
	query params  | date range query params | pagination params  | order params
	------------------------------------------------------------------------------------------------------------------
	?param=foo    | ?param=[from, to]       | ?limit=10,offset=1 | ?ordering=columns_name(asc), ordering=-columns_name (desc) 





### aws doc for deployment

https://github.com/monetree/aws-deployment/blob/master/django-aws-deployment.md
