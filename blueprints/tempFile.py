static createGraph() {
        const allInactiveCredits = CreditDeletion.getInactiveCredits()
        const lastUsedOptions = {"30+":2592000,"60+":5184000,"90+":7776000,"4M+":10368000,"5M+":12960000,"6M+":15552000,"7M+":18144000,"8M+":20736000,"9M+":23328000,"10M+":25920000,"11M+":28512000,"1Y+":31104000}

        for (let j = 0; j < lastUsedOptions.length; j++){
            for (let i = 0; i < allInactiveCredits.length; i++) {
                while (allInactiveCredits[i][1] < lastUsedOptions[j])
                allInactiveCredits[i][1]
            }
        }


def createGraph():
    allInactiveCredits = [('2113b1272730400d', 1202030081), ('7e2a4fbf13434bee', 1690030081), ('bff73ba993b94b5f', 1690030081), ('b0894ee902774336', 1690030081), ('6c3a4f761743426d', 1690030081), ('dbfa2b75f6bc4f21', 1690030081), ('d116ba6a41c1454e', 1690030081), ('11382de066474954', 1690030081)]
    lastUsedOptions = {"30+":2592000,"60+":5184000,"90+":7776000,"4M+":10368000,"5M+":12960000,"6M+":15552000,"7M+":18144000,"8M+":20736000,"9M+":23328000,"10M+":25920000,"11M+":28512000,"1Y+":31104000}

    for i in allInactiveCredits:
        if (allInactiveCredits[i][1]-lastUsedOptions["30+"]) < (currentTime-lastUsedOptions["30+"]):

            if (allInactiveCredits[i][1]-lastUsedOptions["60+"]) < (currentTime-lastUsedOptions["60+"]):

                if (allInactiveCredits[i][1]-lastUsedOptions["60+"]) < (currentTime-lastUsedOptions["90+"]):

                    if (allInactiveCredits[i][1] - lastUsedOptions["60+"]) < (currentTime - lastUsedOptions["4M+"]):

                        if (allInactiveCredits[i][1] - lastUsedOptions["60+"]) < (currentTime - lastUsedOptions["4M+"]):

            else:



