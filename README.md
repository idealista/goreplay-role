# GOR role

This ansible role installs and configure go replay.

To enable gor and replicate traffic on another host

```bash
gor_input: --input-raw :80
gor_output: --output-http=http://test01:80
gor_enabled: True
```

To save it to a file

```bash
gor_input: --input-raw :80
gor_output: "--output-file={{ gor_output_dir }}/requests.gor"
gor_enabled: True
```

!Stop gor to retrieve the file, otherwise you could lost last requests https://github.com/buger/gor/wiki/Saving-and-Replaying-from-file#buffered-file-output

```bash
gor_enabled: False
```

Or stop the service manually

```bash
ssh user@host
sudo service gor stop
```

Or start the service with a low flush interval

```bash
gor_input: --input-raw :80
gor_output: "--output-file={{ gor_output_dir }}/requests.gor"
gor_enabled: True
gor_options:
  - output-file-flush-interval 0m1s
```

To launch tests

```bash
molecule test
```
