# Chaos Toolkit extension for Dynatrace

[![Build Status](https://travis-ci.org/chaostoolkit-incubator/chaostoolkit-dynatrace.svg?branch=main)](https://travis-ci.org/chaostoolkit-incubator/chaostoolkit-dynatrace)

[Dynatrace][dynatrace] support for the [Chaos Toolkit][chaostoolkit].

[dynatrace]: https://www.dynatrace.es/
[chaostoolkit]: http://chaostoolkit.org/

## Install

To be used from your experiment, this package must be installed in the Python
environment where [chaostoolkit][] already lives.

[chaostoolkit]: https://github.com/chaostoolkit/chaostoolkit

```
$ pip install chaostoolkit-dynatrace
```

## Usage

To use this package, you must create have access to a Dynatrace instance via
[DynatraceApi][]  and be allowed to connect to it.

[DynatraceApi]:https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication/

the access credentials to the api must be specified in the configuration section

```json
{

    "configuration": {
        "dynatrace": {
            "dynatrace_base_url": $dynatrace_base_url,
            "dynatrace_token": $dynatrace_token
        }
    }
}
```

This package only exports probes to get some aspects of your system 
monitored by Dynatrace.

Here is an example of how to get the failure rate of a service in Dynatrace.
for this example, the api for validate de failure rate is [Metric-v1][]
[Metric-v1]:https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v1/


```json
{
    "type": "probe",
    "name": "get-failure-rate-services",
    "provider": {
        "type": "python",
        "module": "chaosdynatrace.probes",
        "func": "failure_rate",
        "arguments": {
            "entity": "SERVICE-665B05BC92550119",
            "relative_time":"30mins",
            "faile_percentage": 1
        }
    }
}
```

The probe returns true if the api request failure percentage is less than 
"faile_percentage" or raises an exception when an error is met.


The result is not further process and should be found in the generated report
of the experiment run.

## Contribute

If you wish to contribute more functions to this package, you are more than
welcome to do so. Please, fork this project, make your changes following the
usual [PEP 8][pep8] code style, sprinkling with tests and submit a PR for
review.

[pep8]: https://pycodestyle.readthedocs.io/en/latest/

### Develop

If you wish to develop on this project, make sure to install the development
dependencies. But first, [create a virtual environment][venv] and then install
those dependencies.

[venv]: http://chaostoolkit.org/reference/usage/install/#create-a-virtual-environment

```console
$ pip install -r requirements-dev.txt -r requirements.txt 
```

Then, point your environment to this directory:

```console
$ python setup.py develop
```

Now, you can edit the files and they will be automatically be seen by your
environment, even when running from the `chaos` command locally.

### Test

To run the tests for the project execute the following:

```
$ pytest
```

### Add new Dynatrace API Support

Once you have setup your environment, you can start adding new
[Dynatrace API support] [dynatraceapi] by adding new actions, probes and entire sub-packages
for those.

[dynatraceapi]: https://www.dynatrace.com/support/help/dynatrace-api