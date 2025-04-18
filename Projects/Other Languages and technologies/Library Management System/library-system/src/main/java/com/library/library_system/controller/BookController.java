package com.library.library_system.controller;

import com.library.library_system.model.Book;
import com.library.library_system.repository.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/books")
public class BookController {
@Autowired
private BookRepository bookRepository;
//get all books
@GetMapping  
public List<Book> getAllBooks() {
    return bookRepository.findAll();
}
}
