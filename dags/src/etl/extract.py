import requests
from bs4 import BeautifulSoup
import pandas as pd

URL_MENU = "https://www2.susep.gov.br/menuestatistica/RankRoubo/menu1.asp"
URL_RESP_BASE = "https://www2.susep.gov.br/menuestatistica/RankRoubo/resp_menu1.asp"

def run_extract(cod_tarif: str, regiao: str, ano_modelo: str = "", sexo: str = "Todos", idade: str = "Todas") -> pd.DataFrame:
    regiao_dict = {"RJ - Capital": "18"}

    s = requests.Session()
    s.verify = False

    # abre a página inicial para gerar cookie
    s.get(URL_MENU, verify=False)

    # consulta
    html = s.get(
        URL_RESP_BASE 
        + f"?cod_tarif={cod_tarif}&regiao={regiao_dict[regiao]}&ano_modelo=&sexo={sexo}&idade={idade}&ordenacao=1&id=&Submit=Processar",
        verify=False,
    )
    soup = BeautifulSoup(html.text, "html.parser")
    colunas = ["Modelo", "Índice de Roubos/Furtos (%)", "Veículos Expostos", "N° de Sinistros"]

    rows = []
    table_rows = soup.find_all("tr")

    for tr in table_rows:
        tds = tr.find_all("td")
        if not tds:
            continue
        row = [td.get_text(strip=True) for td in tds]
        rows.append(row)
    df = pd.DataFrame(rows, columns=colunas)
    return df

if __name__ == "__main__":
    run_extract()
