"""
Import as:

import vendors_amp.ib.data.load.sql_data_loader as vidlsq
"""
import helpers.dbg as dbg
import instrument_master.common.data.load.sql_data_loader as vcdlsq
import instrument_master.common.data.types as vcdtyp


class IbSqlDataLoader(vcdlsq.AbstractSqlDataLoader):
    @staticmethod
    def _get_table_name_by_frequency(frequency: vcdtyp.Frequency) -> str:
        """
        Get table name by predefined frequency.

        :param frequency: a predefined frequency
        :return: table name in DB
        """
        table_name = ""
        if frequency == vcdtyp.Frequency.Minutely:
            table_name = "IbMinuteData"
        elif frequency == vcdtyp.Frequency.Daily:
            table_name = "IbDailyData"
        elif frequency == vcdtyp.Frequency.Tick:
            table_name = "IbTickData"
        dbg.dassert(table_name, f"Unknown frequency {frequency}")
        return table_name