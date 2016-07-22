var pug = require('gulp-pug');
var gulp = require('gulp');

gulp.task('views', function buildHTML() {
  return gulp.src('assets/**/*.pug')
  .pipe(pug({
    pretty: true
    // Your options in here.
  }))
  .pipe(gulp.dest('public_html/'))
});

gulp.task('watch', function(){
  gulp.watch('assets/**/*.pug', ['views']);
});

gulp.task('default', ['views', 'watch']);
