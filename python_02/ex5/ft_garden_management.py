#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"{self.message}"


class AddPlantError(GardenError):
    def __str__(self) -> str:
        return f"{self.message}"


class WaterError(GardenError):
    def __str__(self) -> str:
        return f"{self.message}"


class SunlightError(GardenError):
    def __str__(self) -> str:
        return f"{self.message}"


class CheckHealthProblem(GardenError):
    def __str__(self) -> str:
        return f"{self.message}"


class Plant:
    def __init__(self, name: str, water: int = 5, sun: int = 5) -> None:
        self.name = name
        self.water = water
        self.sun = sun

    def display_info(self) -> None:
        print(f"{self.name} - water: {self.water}, sun: {self.sun}")


class GardenManager:
    def __init__(self, garden: list) -> None:
        self.garden = garden

    def add_plants(self, plants_name: list) -> None:
        for plant in plants_name:
            try:
                if not plant or plant == "":
                    raise AddPlantError("Plant name cannot be empty!")
                else:
                    plant = Plant(plant)
                    self.garden.append(plant)
                    print(f"Added {plant.name} successfully")
            except AddPlantError as e:
                print(f"Error adding plant: {e}")

    def water_plant(self,
                    desired_plant: str,
                    add_water_lvl: int) -> None:
        print("Opening watering system")
        try:
            plant_found = False
            if add_water_lvl < 1:
                raise WaterError("Cannot add 0 or negative water")
            for plant in self.garden:
                if plant.name == desired_plant:
                    plant_found = True
                    plant.water += add_water_lvl
                    print(f"Watering {plant.name} - success")
            if not plant_found:
                raise NameError(f"Garden does not contain {desired_plant}")

        except (WaterError, NameError) as e:
            print(f"Error adding water: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def water_all_plant(self, add_water_lvl: int) -> None:
        print("Opening watering system")
        try:
            if add_water_lvl < 1:
                raise WaterError("Cannot add 0 or negative water")
            for plant in self.garden:
                plant.water += add_water_lvl
                print(f"Watering {plant.name} - success")

        except (WaterError, NameError) as e:
            print(f"Error adding water: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def expose_to_sun(self, desired_plant: str, hours: int) -> None:
        """Expose specific plant to sun"""
        print("=== Opening spot on roof system ===")
        try:
            plant_found = False
            if hours < 1:
                raise SunlightError("Cannot open for 0 or negative hours.")
            for plant in self.garden:
                if plant.name == desired_plant:
                    plant_found = True
                    plant.sun += hours
                    print(f"{plant.name} exposed to sun - success")
            if not plant_found:
                raise NameError(f"Garden does not contain {desired_plant}")

        except (NameError, SunlightError) as e:
            print(f"Error oppening roof: {e}")
        finally:
            print("=== Closing spot on roof system ===\n")

    def expose_all_to_sun(self, hours: int) -> None:
        """Expose all plants to sun"""
        print("=== Opening general roof system ===")
        try:
            if hours < 1:
                raise SunlightError("Cannot oppen for 0 or negative hours.")
            else:
                for plant in self.garden:
                    plant.sun += hours
                    print(f"{plant.name} exposed to sun - success")
        except SunlightError as e:
            print(f"Error oppening roof: {e}")
        finally:
            print("=== Closing general roof system ===\n")

    def check_plant_health(self, desired_plant: str) -> None:
        """Validates plant health parameters"""

        print(f"=== Starting plant health check for {desired_plant} ===")
        try:
            plant_found = False
            for plant in self.garden:
                if plant.name == desired_plant:
                    plant_found = True
                    if plant.water < 1 or plant.water > 10:
                        raise CheckHealthProblem(
                            f"Water level {plant.water} is too high (max 10)"
                        )
                    if plant.sun < 2 or plant.sun > 12:
                        raise CheckHealthProblem(
                            f"Sunlight {plant.sun} is out of range (2-12)"
                        )
                    print(f"{plant.name}: healthy (water: {plant.water}, "
                          f"sun: {plant.sun})")
                    return

            if not plant_found:
                raise NameError(f"Garden does not contain {desired_plant}")

        except (CheckHealthProblem, NameError) as e:
            print(f"Error checking {desired_plant}: {e}")
        except NameError as e:
            print(f"Error: {e}")
        finally:
            print("=== Closing specific plant health check ===\n")

    def check_all_health(self) -> None:
        try:
            if not self.garden:
                print("The garden is currently empty.")
                return

            for plant in self.garden:
                try:
                    if plant.water < 1 or plant.water > 10:
                        raise CheckHealthProblem(
                            f"Water level {plant.water} is out of range (1-10)"
                        )
                    if plant.sun < 2 or plant.sun > 12:
                        raise CheckHealthProblem(
                            f"Sunlight {plant.sun} is out of range (2-12)"
                        )

                    print(
                        f"{plant.name}: healthy (water: {plant.water}, "
                        f"sun: {plant.sun})"
                    )

                except CheckHealthProblem as e:
                    print(f"Error checking {plant.name}: {e}")

                finally:
                    print(f"Status sync for {plant.name} complete.")

        except Exception as e:
            print(f"Critical System Error: {e}")

        finally:
            print("=== Garden Health Check Complete ===\n")


# Util Wraper
def test_garden_management() -> None:
    print("===== Garden Management System =====\n")

    crop = []
    my_garden = GardenManager(crop)

    print("Adding plants to garden...")
    my_garden.add_plants(["tomato", "lettuce", "", "carrot"])

    print("\nWatering plants...")
    my_garden.water_plant("tomato", 2)
    my_garden.water_plant("parseley", 2)
    my_garden.water_all_plant(2)
    my_garden.water_all_plant(-1)

    print("\nExposing plants to sun...")
    my_garden.expose_to_sun("lettuce", 2)
    my_garden.expose_to_sun("parsley", 2)
    my_garden.expose_all_to_sun(2)
    my_garden.expose_all_to_sun(-1)

    print("\nChecking plant health...")
    my_garden.check_plant_health("tomato")
    my_garden.water_plant("tomato", 10)
    my_garden.check_plant_health("tomato")
    my_garden.check_plant_health("parsley")

    my_garden.check_all_health()

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
