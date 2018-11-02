
from MedLearn.common import CorrStat
CorrStat_conf = CorrStat().get_info()

GlobalConf = [
        {"id": "comman",
        "name": "通用方法",
        "children": [CorrStat_conf]
        }
        ]
                        