export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!students.every((student) => typeof student === 'string')) {
      throw new TypeError('Students array must contain only strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  // name
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // length
  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  // students
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
