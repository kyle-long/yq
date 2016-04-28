yq
==

Utility that wraps [jq](https://stedolan.github.io/jq/).  All it does is decode yaml and passes it along to jq.

Note: These packages do not force you to have jq (at least not yet)

Bigger Note: So far this is just a hacky script.  Expect issues.

Build .deb
----------

```
pip install -r requirements.txt
python setup.py --command-packages=stdeb.command sdist_dsc
cd deb_dist/ya-<version>
dpkg-buildpackage
```

Build .rpm
----------
```
python setup.py bdist_rpm
```

Test .rpm
---------
```
cd dist
rpm -ivh yq<version>.noarch.rpm
```
