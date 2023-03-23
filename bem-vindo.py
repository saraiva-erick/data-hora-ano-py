import datetime

# Pré-requisitos: Phyton

# mensagem de boas-vindas
print("Bem-vindo(a) ao aplicativo de data e hora em Python!")

# Obter a data e hora atual
now = datetime.datetime.now()

# Apresentar o dia da semana e a data
print("Hoje é", now.strftime("%A"), ", ", now.strftime("%d/%m/%Y"))

# Calcular quantos dias restam até o final do ano
end_of_year = datetime.datetime(now.year, 12, 31)
days_left = (end_of_year - now).days

# Apresentar a quantidade de dias restantes e já percorridos no ano
print("Já passaram", now.timetuple().tm_yday, "dias neste ano e restam", days_left, "dias até o final do ano.")
