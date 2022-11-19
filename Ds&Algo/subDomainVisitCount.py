# https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        #basic hash
        dom_cnt = {}
        for domain in cpdomains:
            c_doms = domain.split(" ")
            cnt = int(c_doms[0])
            full_dom = c_doms[1]
            sub_doms = c_doms[1].split(".")
            doms_list = [f'{i}.{sub_doms[-1]}' for i in sub_doms[-2:-1]]
            if full_dom not in doms_list:
                doms_list += [full_dom, sub_doms[-1]]
            else:
                doms_list += [sub_doms[-1]]
            for d in doms_list:
                if d in dom_cnt.keys():
                    dom_cnt[d]+=cnt
                else:
                    dom_cnt[d] = cnt
        out_list = []
        for k in list(dom_cnt.keys()):
            out_list.append(f'{dom_cnt[k]} {k}')
        return out_list