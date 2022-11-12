import pandas as pd
import pycep_correios
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


# Função para transformar o CEP em um endereço
def get_address(cep):
    try:
        endereco = pycep_correios.get_address_from_cep(cep)
        return endereco['logradouro'] + ", " + endereco['bairro'] + ", " + endereco['cidade'] + " - " + endereco['uf']
    except:
        #print('CEP não encontrado')
        return None

def get_location(endereco):
    geolocator = Nominatim(user_agent="test_app")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    df = {}
    df['endereco'] = endereco
    print(df['endereco'])
    df['location'] = df['endereco'].apply(geocode)
    df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
    pontos = df['point']
    return pontos

# DataFrame de teste
#df = pd.DataFrame({'CEP': []})

# Troque test_app pelo nome da sua aplicação/sistema
#geolocator = Nominatim(user_agent="pji3g54app")
#geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Cria a coluna address com os endereços retornados a partir do CEP
#df['address'] = df['CEP'].apply(get_address)

# Cria a coluna location com o local retornado a partir do endereço
#df['location'] = df['address'].apply(geocode)

# Seleciona a latitude e longitude que está dentro do local
#df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
#print(df)
#print(df['address'])
