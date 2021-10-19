# Action to create a dynamic badge

This action allows to create those beautiful badges in the README.md file without having to create
new pull request everytime there is an update.

The action is enabled with [shields.io](https://shields.io/endpoint) and supports all the
possibilites in the endpoint. It will change any time the actions is run so it will adapt quickly
to the new situation.


## How to use it

Whenever the action is triggered, it will generate a new json document that will be stored in the
gist of the user. From there the _shields.io_ endpoint will ingest that json document and render
the appropriate badge in the README.md file.

The configuration is defined by the _imgshields.io_ endpoint and follow the structure below:

```json
{
  "schemaVersion": 1,
  "label": "hello",
  "message": "sweet world",
  "color": "orange"
}
```


## Configuration

1. Create a secret token to access the gist
2. Add the secret to the secrets in the proejct repository
3. Create a gist and record the gist_id
4. Add the following to the workflow file:
```yaml
      - name: Create the Badge
        uses: loicdiridollou/dyn-badge-action@main
        with:
          secret: ${{ secrets.GIST_SECRET }}
          gist_id: GIST_ID
          filename: FILENAME
          message: MESSAGE
          color: COLOR
          value: VALUE
          user: USERNAME
```
