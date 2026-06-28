class Solution:

    def encode(self, strs: List[str]) -> str:
        return "-".join(strs) if strs!=[] else "flag"

    def decode(self, s: str) -> List[str]:
        p=s.split("-")
        return p if p!=["flag"] else []