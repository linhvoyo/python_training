
identities = []
for i in result.alignments:
    for k in i.hsps:
        identities.append(k.identities)

print filter(lambda x: 100 *  x[0]/x[1] > 50 , identities)