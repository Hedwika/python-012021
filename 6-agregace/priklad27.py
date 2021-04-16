import pandas
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

# Pokračuj ve své práci pro softwarovou firmu. Ze souboru vykazy.csv načti informace o výkazech na projekty pro jednoho vybraného zákazníka.
# - Načti data ze souboru a ulož je do tabulky.
vykazy = pandas.read_csv('vykazy.csv')

# - Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.
hodiny = vykazy.groupby('project').sum("hours")
hodiny = hodiny.drop(columns="emloyee_id")
print(f"Celkový počet vykázaných hodin na jednotlivé projekty byl:\n{hodiny}")

# Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení. Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře, tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.
vykazy.columns = ['datum', 'hodiny', 'projekty', 'cislo_zamestnance']
zamestnanci = pandas.read_csv('zamestnanci.csv')
zamestnanci_projekty = pandas.merge(zamestnanci, vykazy, on=['cislo_zamestnance'])
hodiny_kancelare = zamestnanci_projekty.groupby('město').sum("hours")
hodiny_kancelare = hodiny_kancelare.drop(['cislo_zamestnance', 'Unnamed: 0'], axis = 1)
print(f"\nCelkový počet vykázaných hodin byl v jednotlivých kancelářích následující:\n{hodiny_kancelare}")