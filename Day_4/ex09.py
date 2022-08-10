def numUniqueEmails(emals):
    local_name = []
    domain_name = []
    new_emals = []
    j = 0
    for i in emals:
        local_name.append(i.split('@')[0])
        domain_name.append(i.split('@')[1])
        if local_name[j].find(".") != -1:
            local_name[j] = local_name[j].replace('.', '')
        if local_name[j].find("+") != -1:
            local_name[j] = local_name[j][:local_name[j].index('+')]
        new_emals.append(local_name[j] + '@' + domain_name[j])
        j += 1
    return len(set(new_emals))