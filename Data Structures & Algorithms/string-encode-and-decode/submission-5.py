class Solution:

    def encode(self, strs: List[str]) -> str:
        return "😀".join(strs) if len(strs) > 0 else "😁"

    def decode(self, s: str) -> List[str]:
        if s=="😁":
            return []
        else:
            return s.split("😀") if len(s)>0 else [""]
