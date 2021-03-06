# NOTICE: Generated By HttpRunner. DO NOT EDIT!
# FROM: examples/httpbin/validate.yml

from httprunner import HttpRunner, TConfig, TStep


class TestCaseValidate(HttpRunner):
    config = TConfig(
        **{
            "name": "basic test with httpbin",
            "base_url": "http://httpbin.org/",
            "path": "examples/httpbin/validate_test.py",
            "variables": {},
        }
    )

    teststeps = [
        TStep(
            **{
                "name": "validate response with json path",
                "request": {"url": "/get", "params": {"a": 1, "b": 2}, "method": "GET"},
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.args.a", 1]},
                    {"eq": ["body.args.b", 2]},
                ],
                "validate_script": ["assert status_code == 200"],
            }
        ),
        TStep(
            **{
                "name": "validate response with python script",
                "request": {"url": "/get", "params": {"a": 1, "b": 2}, "method": "GET"},
                "validate": [{"eq": ["status_code", 200]}],
                "validate_script": [
                    "assert status_code == 201",
                    "a = response_json.get('args').get('a')",
                    "assert a == '1'",
                ],
            }
        ),
    ]


if __name__ == "__main__":
    TestCaseValidate().test_start()
