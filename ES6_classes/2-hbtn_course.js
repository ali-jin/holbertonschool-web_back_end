export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof(name) != 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof(length) != 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!students.every((student) => typeof student === 'string')) {
      throw new TypeError('Students array must contain only strings');
    }

    this._name = name;
    this._lenght = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof(value) != 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  get length() {
    return this._lenght;
  }

  set length(value) {
    if (typeof(value) != 'number') {
      throw new TypeError('Length must be a number');
    }
    this._lenght = value;
  }

  get students() {
    return this._students;
  }

  set students(value) {
    if (!value.every((student) => typeof student === 'string')) {
      throw new TypeError('Students array must contain only strings');
    }
    this._students = value;
  }
}
