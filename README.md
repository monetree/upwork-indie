# Api documentation 

### query params standard
                    
	query params  | date range query params | pagination params  | order params
	------------------------------------------------------------------------------------------------------------------
	?param=foo    | ?param=[from, to]       | ?limit=10,offset=1 | ?ordering=columns_name(asc), ordering=-columns_name (desc) 




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
                    





### aws doc for deployment

https://github.com/monetree/aws-deployment/blob/master/django-aws-deployment.md


## reference for frontend developer


### html embed code - encoder

```javascript
const btoaUTF16  = (sString) => {
    var aUTF16CodeUnits = new Uint16Array(sString.length);
    Array.prototype.forEach.call(aUTF16CodeUnits, function (el, idx, arr) { arr[idx] = sString.charCodeAt(idx); });
    return btoa(String.fromCharCode.apply(null, new Uint8Array(aUTF16CodeUnits.buffer)));
  }
```


### html embed code - deencoder

```javascript
const atobUTF16 =  (sBase64) => {
    var sBinaryString = atob(sBase64), aBinaryView = new Uint8Array(sBinaryString.length);
    Array.prototype.forEach.call(aBinaryView, function (el, idx, arr) { arr[idx] = sBinaryString.charCodeAt(idx); });
    return String.fromCharCode.apply(null, new Uint16Array(aBinaryView.buffer));
  }
  }
```
