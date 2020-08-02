"""
Abstract Factory Pattern: This pattern is a factory of factories
For example: FactorProducer calls another
factory(manufacture_type) which again makes a call to
VehicleFactory(vehicle_type).
"""

from abc import ABC, abstractmethod
################# Factory Producer or Customer ##############
class FactoryProducer:
	def get_factory(manufacturer_type):
		if manufacturer_type == 'Maruti Suzuki':
			return MarutiFactory
		elif manufacturer_type == 'Tesla Inc':
			return TeslaFactory
################ Factories - Maruti and Tesla ###############
class Factory(ABC):
	@abstractmethod
	def get_vehicle(self):
		pass

class MarutiFactory(Factory):
	manufacturer = "Maruti Suzuki"

	def get_vehicle(vehicle_type):
		if vehicle_type == 'Car':
			return BalenoCar()
		elif vehicle_type == 'Bike':
			return BulletBike()

class TeslaFactory(Factory):
	manufacturer = "Tesla Inc"

	def get_vehicle(vehicle_type):
		if vehicle_type == 'Car':
			return TeslaCar()
		elif vehicle_type == 'Bike':
			return SplendorPlusBike()

################ Vehicle Factory - Car and Bike ###############
class VehicleFactory(ABC):
	@abstractmethod
	def assemble(self):
		pass

class BalenoCar(VehicleFactory):
	name = "Baleno"

	def assemble(self):
		return "Car: %s is ready" % self.name

class BulletBike(VehicleFactory):
	name = "Bullet"

	def assemble(self):
		return "Bike: %s is ready" % self.name

class TeslaCar(VehicleFactory):
	name = "Tesla Model xv"

	def assemble(self):
		return "Car: %s is ready" % self.name

class SplendorPlusBike(VehicleFactory):
	name = "Splendor Plus"

	def assemble(self):
		return "Bike: %s is ready" % self.name

def main():
	"""
	>>> teslafactory = FactoryProducer.get_factory("Tesla Inc")
	>>> teslacar = teslafactory.get_vehicle('Car')
	>>> print(teslacar.assemble())
	Car: Tesla Model xv is ready
	"""

if __name__ == '__main__':
	import doctest
	doctest.testmod()