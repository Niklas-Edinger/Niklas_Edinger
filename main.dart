class Class {
  var myProperty = 'Hello, World!';
  myMethod() {
    print(this.myProperty);
  }
}

void main() {
  Class().myMethod();
}