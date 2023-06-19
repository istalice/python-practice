class Solution:
    """
    @param c: A character.
    @return: The character is alphanumeric or not.
    """

    def is_alphanumeric(self, c: str) -> bool:
        ch = c[0]
        return '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'
