export default function createInt8TypedArray(lenght, position, value) {
  if (position >= lenght) {
    throw new Error("Position outside range");
  }
  const buffer = new ArrayBuffer(length);
  const view = new Int8Array(buffer);
  view[position] = value;
  return new DataView(buffer);
}
