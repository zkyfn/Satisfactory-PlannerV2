from dearpygui.dearpygui import *

# 示例数据，item列表
items = [
    "Iron Ore",
    "Copper Ore",
    "Caterium Ore",
    "Raw Quartz",
    "Coal",
    "Water",
    "Nitrogen Gas",
    "Sulfur",
    "Bauxite",
    "Uranium",
    "Limestone",
    "Crude Oil",
    "SAM"
]

# 示例配方数据
regular_recipes = ["Smelting", "Refining", "Assembly"]
alternate_recipes = ["Alternate Smelting", "Alternate Refining", "Alternate Assembly"]

# 控制alternate全选回调
def toggle_all_alternate(sender, app_data):
    for alt in alternate_recipes:
        set_value(f"chk_alt_{alt}", app_data)

def build_gui():
    with window(label="Satisfactory Planner", width=1000, height=800):
        with tab_bar():

            # Planner Tab
            with tab(label="Planner"):
                add_text("Inputs")
                add_combo(items, label="Item Select", tag="input_item_combo")
                add_input_int(label="Number of Input", tag="input_quantity")
                add_button(label="Add Input")
                add_button(label="Remove Input")

                add_spacer(height=10)
                add_text("Outputs")
                add_combo(items, label="Item Select", tag="output_item_combo")
                add_input_int(label="Number of Output", tag="output_quantity")
                add_button(label="Add Output")
                add_button(label="Remove Output")

                add_spacer(height=10)
                add_button(label="Run Optimization")
                add_button(label="Save Settings")
                add_button(label="Load Settings")
                add_button(label="Reset")

            # Settings Tab
            with tab(label="Settings"):
                add_text("Resource Limits")
                resources = {
                    "Water": 100000,
                    "Caterium Ore": 15000,
                    "Raw Quartz": 13500,
                    "Coal": 42300,
                    "Nitrogen Gas": 12000,
                    "Iron Ore": 92100,
                    "Sulfur": 10800,
                    "Bauxite": 12300,
                    "Uranium": 2100,
                    "Limestone": 69900,
                    "Crude Oil": 12600,
                    "Copper Ore": 36900,
                    "SAM": 10200
                }
                for res, default in resources.items():
                    add_input_int(label=res, default_value=default)

                add_spacer(height=10)
                add_text("Weights")
                weights = [
                    ("Power Use", 0.3),
                    ("Item Use", 0.4),
                    ("Building Use", 0.0),
                    ("Resource Use", 0.0),
                    ("Building Scaled", 30.0),
                    ("Resources Scaled", 1.0),
                    ("Nuclear Waste", 9999999.0)
                ]

                with table(header_row=False, borders_innerV=True, row_background=True, resizable=True):
                    add_table_column(width_fixed=True)
                    add_table_column(width_fixed=True)
                    add_table_column(width_fixed=True)

                    for name, default_val in weights[:-1]:
                        with table_row():
                            add_text(name)
                            add_input_float(label="", default_value=default_val, width=100, tag=f"weight_{name.lower().replace(' ', '_')}")
                            add_button(label="Info", width=50)
                    # Nuclear Waste
                    with table_row():
                        add_text(weights[-1][0])
                        add_input_float(label="", default_value=weights[-1][1], width=100, tag="weight_nuclear_waste")
                        add_button(label="Info", width=50)
                    add_checkbox(label="Penalize Plutonium Fuel Rods", tag="penalize_plutonium")

                add_spacer(height=10)
                add_text("Recipes")

                add_checkbox(label="Alternate Recipes (Select All)", callback=toggle_all_alternate, tag="chk_alt_select_all", default_value=True)

                add_text("Regularly Unlocked Recipes:")
                for r in regular_recipes:
                    add_checkbox(label=r, tag=f"chk_reg_{r}", default_value=False)
                    add_same_line()

                add_spacer(height=10)
                add_text("Alternate Recipes:")
                for a in alternate_recipes:
                    add_checkbox(label=a, tag=f"chk_alt_{a}", default_value=True)
                    add_same_line()

            # Results Tab
            with tab(label="Results"):
                add_text("Products")
                add_input_text(multiline=True, width=800, height=200, tag="products_map")
                add_spacer(height=10)
                add_text("Ingredients")
                add_input_text(multiline=True, width=800, height=200, tag="ingredients_map")

create_context()
create_viewport(title='Satisfactory Planner', width=1024, height=768)
build_gui()
setup_dearpygui()
show_viewport()
start_dearpygui()
destroy_context()
