# Doctor Droid Python Transporter

The present repository contains the source code of the Doctor Droid Transporter Agent version 1.0.0.
Read more [here](https://docs.drdroid.io/docs).

## Documentation

The Agent runs inside your VPC and acts as a reverse proxy to connect with your metric sources and send
metrics and related data to doctor droid platform.

Currently, the agent supports the following metric sources in your VPC:

* Grafana

## Env vars

| Env Var Name      | Description                                    | Required | 
|-------------------|------------------------------------------------|----------|
| DRDROID_API_TOKEN | Authentication token for doctor droid platform | True     |
| GRAFANA_HOST      | Grafana host accessible within VPC             | False    |
| GRAFANA_API_KEY   | Grafana API Token                              | False    |

## Configuration

Identify the auth token needed for the authenticating http calls between doctor droid platform and agent by
visiting [site](https://playbooks.drdroid.io/api-keys)
Once auth token is available, you can set the env var as:

```shell
DRDROID_API_TOKEN=<API_TOKEN> GRAFANA_HOST=<HOST> GRAFANA_API_KEY=<KEY> docker-compose -f agent.docker-compose.yml up
```

## Support

Visit [Doctor Droid website](https://drdroid.io?utm_param=github-py) for getting early access.
Go through our [documentation](https://docs.drdroid.io?utm_param=github-py) to learn more.

For any queries, reach out at [dipesh@drdroid.io](mailto:dipesh@drdroid.io).
