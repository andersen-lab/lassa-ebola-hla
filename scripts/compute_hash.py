import pandas as pd
import hashlib

ledger = pd.read_csv("ledger.csv", index_col = 0)
gen = pd.read_csv("../Genotype_calls.csv")

new_ledger = {
    "HASH": [],
    "ID": []
}
for i in gen.index:
    _ = ledger[ledger["ID"]==gen.ix[i]["ID"]]
    if _.shape[0] == 0:
        m = hashlib.md5()
        m.update(gen.ix[i]["ID"].encode("utf-8"))
        new_ledger["HASH"].append(m.hexdigest())
        new_ledger["ID"].append(gen.ix[i]["ID"])

ledger = pd.concat([ledger, pd.DataFrame(new_ledger)]).reset_index(drop=True)
gen = gen.drop("Alternative ID", axis = 1)
gen["ID"] = gen["ID"].apply(lambda x: ledger[ledger["ID"]==x]["HASH"].values[0])
gen.to_csv("../Genotype_calls.csv", index=False)

ledger.to_csv("ledger.csv")
