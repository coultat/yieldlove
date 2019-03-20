def date_format(value):
    months = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
    month = months[value.month - 1]
    return "{} de {} de {}".format(value.day, month, value.year)
