export default function getStudentsByLocation(arrayStudent, city) {
  return arrayStudent.filter((student) => student.location === city);
}
