class Vehicle {
    getType(): string {
        throw new Error('getType method must be overridden');
    }
}

class Car extends Vehicle {
    getType(): string {
        return 'Car';
    }
}

class Bike extends Vehicle {
    getType(): string {
        return 'Bike';
    }
}

class Truck extends Vehicle {
    getType(): string {
        return 'Truck';
    }
}

abstract class VehicleFactory {
    abstract createVehicle(): Vehicle;
}

class CarFactory extends VehicleFactory {
    // Write your code here
    createVehicle(): Vehicle {
        return new Car();
    }
}

class BikeFactory extends VehicleFactory {
    // Write your code here
    createVehicle(): Vehicle {
        return new Bike();
    }
}

class TruckFactory extends VehicleFactory {
    // Write your code here
    createVehicle(): Vehicle {
        return new Truck()
    }
}
