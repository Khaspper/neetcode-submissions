class LRUCache {
    /**
     * @param {number} capacity
     */
    capacity: number;
    size: number
    myMap: Map<number, number>;
    constructor(capacity: number) {
        this.capacity = capacity;
        this.size = 0;
        this.myMap = new Map<number, number>()
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key: number): number {
        if (this.myMap.has(key)) {
            const value: number = this.myMap.get(key);
            this.moveToEnd(key, value);
            return value
        }
        return -1
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key: number, value: number): void {
        if (this.myMap.has(key)) {
            this.moveToEnd(key, value)
            return
        }
        this.size = this.size + 1
        if (this.size > this.capacity) {
            this.removeLRU()
        }
        this.myMap.set(key, value)
    }

    moveToEnd(key: number, value: number): void {
        this.myMap.delete(key)
        this.myMap.set(key, value)
    }

    removeLRU(): void {
        this.size = this.size - 1;
        const LRUKey: number = this.myMap.keys().next().value;
        this.myMap.delete(LRUKey)
    }
}
