yq
==

Utility that wraps [jq](https://stedolan.github.io/jq/).  All it does is decode yaml and passes it along to jq.

Note: These packages do not force you to have jq (at least not yet)

Bigger Note: So far this is just a hacky script.  Expect issues.

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

Install with pip (why not?)
---------------------------
```
pip install git+git://github.com/kyle-long/yq.git@master
```

Usage
-----

Should be the same as jq.  Here are some examples.

```
# pretty print as yaml
cat test.yaml | yq -r .

# pretty print as yaml again
yq -r . test.yaml

# select just the property `blah`
ya -r .blah test.yaml
```

This will output YAML.  If you'd like JSON returned you can provide the `-j` or `--json` options.
```
yq -j -r . test.yaml
```
