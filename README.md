# CRUD Job Space

link API: https://crud-job-space-ps.herokuapp.com/

## POST /api/leads - Rota responsável pelo CADASTRO do usuário.

### Corpo da requisição:

```json
{
  "name": "Suellen Suzuky",
  "email": "suzuky@mail.com",
  "phone": "(77)98800-4948",
  "cep": "45000000",
  "number": "4",
  "placeLog": "Praça da Sé",
  "complement": "lado ímpar",
  "district": "Sé",
  "localityCity": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "ibge",
  "ddd": "11",
  "siafi": "7107"
}
```

### Corpo da resposta:

```json
{
  "id": 1,
  "name": "Suellen Suzuky",
  "email": "suzuky@mail.com",
  "phone": "(77)98800-4948",
  "cep": "45000000",
  "number": "4",
  "placeLog": "Praça da Sé",
  "complement": "lado ímpar",
  "district": "Sé",
  "localityCity": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "ibge",
  "ddd": "11",
  "siafi": "7107",
  "creation_date": "Mon, 09 May 2022 15:09:18 GMT",
  "last_visit": "Mon, 09 May 2022 15:09:18 GMT",
  "visits": 1
}
```

---

## GET /api/leads/home - Rota responsável por listar todos os usuários.

### Corpo da requisição:

    SEM CORPO

### Corpo da resposta:

```json
[
  {
    "id": 3,
    "name": "Suellesdfadfasdfasdfasdfndddd Suzuky",
    "email": "fasdfasdfasdfa@mail.com",
    "phone": "(77)95555-4948",
    "cep": "45000000",
    "number": "4",
    "placeLog": "Praça da Sé",
    "complement": "lado ímpar",
    "district": "Sé",
    "localityCity": "São Paulo",
    "uf": "SP",
    "ibge": "3550308",
    "gia": "ibge",
    "ddd": "11",
    "siafi": "7107",
    "creation_date": "Mon, 09 May 2022 15:09:18 GMT",
    "last_visit": "Mon, 09 May 2022 15:10:49 GMT",
    "visits": 2
  }
]
```

---

## PATCH /api/leads/update - Rota responsável pela ATUALIZAÇÃO de parte das informações do usuário buscando por email.

### Corpo da requisição:

```json
{
  "name": "Nome Editado Suzuky",
  "email": "suzuky@mail.com",
  "newEmail": "novoemail@mail.com",
  "phone": "(77)95555-4948"
}
```

### Corpo da resposta:

```json
{
  "id": 3,
  "name": "Nome Editado Suzuky",
  "email": "novoemail@mail.com",
  "phone": "(77)95555-4948",
  "cep": "45000000",
  "number": "4",
  "placeLog": "Praça da Sé",
  "complement": "lado ímpar",
  "district": "Sé",
  "localityCity": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "ibge",
  "ddd": "11",
  "siafi": "7107",
  "creation_date": "Mon, 09 May 2022 15:09:18 GMT",
  "last_visit": "Mon, 09 May 2022 15:10:49 GMT",
  "visits": 2
}
```

---

## DELETE /api/leads/delete - Rota responsável por deletar as informações do usuário.

### Corpo da resposta:

```json
{
  "email": "novoemail@mail.com"
}
```
