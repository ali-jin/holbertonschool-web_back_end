export default function createInt8TypedArray(lenght, position, value) {
  if (position >= lenght) {
    throw new Error("Position outside range");
  }
  const buffer = new ArrayBuffer(lenght);
  const data = new Int8Array(buffer);
  data[position] = value;
  return new DataView(buffer);
}
