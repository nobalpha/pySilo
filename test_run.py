import dearpygui.dearpygui as dpg

with dpg.window(label="Tutorial"):

    with dpg.table(header_row=False):

        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i in range(0, 4):
            for j in range(0, 3):
                if i == 1 and j == 0 or i == 2 and j == 1:
                    dpg.add_button(label="oh yeassss", height=100, width=50)
                else:
                    dpg.add_text(f"Row{i} Column{j}")
                # call if not last cell
                if not (i == 3 and j == 2):
                    dpg.add_table_next_column()

dpg.start_dearpygui()
