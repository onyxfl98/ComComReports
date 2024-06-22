#!/usr/bin/python3.12

"""Used as the main module for testing purposes"""

#import re
from icecream import install, ic
from get_report_date import get_report_date

install()


def main():
    """Main function executed when this module is directly run"""

    report = get_report_date()

    ic(report)
    
    #print(re.sub(r'\\.',lambda x:{'\\n':'\n','\\t':'\t'}.get(x[0],x[0]),'foo\\nbar\\nbaz\\tbrr\\n\\q'))
    
    #print(re.sub(contents_list)

if __name__ == "__main__":
    main()
