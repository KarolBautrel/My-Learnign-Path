
import time


class HtmlCM:

    def __init__(self):
        pass

    def __enter__(self):
        print("<TABLE>")
        print("<>")
        print("     <TH> Number</TH><TH>Description</TH>")
        print("</TR>")
        return self

    def __exit__(self, exc_type, exc_value, trace):
        print("</TABLE>")


with HtmlCM() as file:
    print(" <TR>")
    print("     <TD>1</TD><TD>Say hello!</TD)")
    print(" </TR>")
    print(" <TR>")
    print("     <TD>2</TD><TD>Say good bye!</TD)")
    print(" </TR>")
