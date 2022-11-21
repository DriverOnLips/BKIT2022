
def one_to_many(conductors, orchectras):
    return [(cond.surname, cond.salary, orch.name)
            for cond in conductors
            for orch in orchectras
            if cond.orch_id == orch.id]


def many_to_many(conductors, orchectras, condOrch):
    return [(cond.surname, cond.salary, orch.name)
            for oc in condOrch
            for cond in conductors
            for orch in orchectras
            if cond.id == oc.id_cond and orch.id == oc.id_orch]
