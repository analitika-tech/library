def get_fields(model:object, exclude:str) -> list:
    fields = []
    for field in model._meta.get_fields():
        if field.name != str(exclude):
            fields.append(field.name)
    return fields