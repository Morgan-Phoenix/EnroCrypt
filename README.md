# EnroCrypt
This is a Python Module For Encryption, Hashing And Other Basic Stuff You Need, With Secure Encryption And Strong Salted Hashing You Can Do Whatever You Want To <br> 
[![Downloads](https://static.pepy.tech/personalized-badge/enrocrypt?period=total&units=international_system&left_color=yellow&right_color=red&left_text=Downloads)](https://pepy.tech/project/enrocrypt)<br><h3>[Docs](https://morgan-phoenix.github.io/EnroCrypt/Docs)</h3>
## Installation
EnroCrypt Is Avaliable On <a style="text-decoration:none;" herf="https://pypi.org/projects/enrocrypt">PyPi </a>You Can Install It As Follows:<br>
```` pip install -U enrocrypt````
## Manual Installation 
If For Some Reason You Can't Install EnroCrypt From PyPi You Can Download It Manually Too:
* Clone This Repo 
* Cut-Paste This Repo In Your Python Scripts Path
* Enter In The Folder Where You See "setup.py" file
* shift+right click in the Folder And Click On "Open Powershell window Here"
* Type `python setup.py install`<br>
After Following All The Steps Mentioned Above (If You Don't Get An Error) EnroCrypt Is Installed, Now You Can Import It Right Away
## Features
* Strong Encryption
* Strong Salted Hashing
* File Encryption-Decryption
* Some Basic Functions
## Usage 
```python
    # For Encryption
    from enrocrypt import core
    obj = core.Core()
    value = obj.Encrypt(b'text')
    print(value)
    # For Decryption
    original_value = obj.DecryptList(value)
    print(original_value)
```
There Is Also a `Decrypt`Function, But In This Function You Have To Enter The Key And The Data Seperatly
## Adding Configurations
Enrocrypt Has The Ablity To Adopt Custom Configurations, Namely:- Custom Salt <br>
We Provide A Function In Which You Can Pass All The Configurations But It Also Has A Syntax And Must Be Used "As is"
```python
from enrocrypt import core
config = {
    'configs':{
        'salt_file':"The Path Of The File Where Your Salt Is Stored"
        }
    }
    # You need a Core Class Object to access that function
    obj = core.Core()
    obj.set_config(config)
```
## Getting A Hashing Class Object
We Suggest Not To Use The Hashing Class By Importing It Directly As If You Do So You Can't Add Your Custom Salt <br>
To Add Custom Salt Follow The `Adding Configuration`. After You Did That You Have To Get A Hasing Class Object By A Core Class Function<br>
```python
from enrocrypt import core
obj = core.Core()
hasing_obj = obj.get_hash_object()
```
(See Discussion For More Info)
